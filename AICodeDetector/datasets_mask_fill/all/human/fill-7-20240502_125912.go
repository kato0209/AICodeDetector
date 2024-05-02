// Package ftp implements a FTP client based on the FTP protocol as
// provided in RFC 959.
//
// A TransferError is returned for errors at the protocol level.
package ftp

import (
	"bufio"
	"context"
	"crypto/tls"
	"errors"
	"io"
	"net"
	"net/textproto"
	"strconv"
	"strings"
	"time"

	"github.com/hashicorp/go-multierror"
)

const (
	// 30 seconds was chosen as it's the
	// same duration as http.DefaultTransport's timeout.
	DefaultDialTimeout = 30 * time.Second
)

// EntryType describes the different ways of creating an Entry.
type EntryType int

// The differents types of an Entry
const (
	EntryTypeFile EntryType = iota
	EntryTypeFolder
	EntryTypeLink
)

// TransferType describes the different formats for transferring Entries.
type TransferType string

// The different transfer types
const (
	TransferTypeBinary = TransferType("I")
	TransferTypeASCII  = TransferType("A")
)

// Time format used by the MDTM and MFMT commands
const timeFormat = "20060102150405"

// ServerConn represents the connection to a remote FTP server.
// A single connection only provides in-flight data ,
// so it is not safe to be called concurrently.
type ServerConn struct {
	options *dialOptions
	conn     connection