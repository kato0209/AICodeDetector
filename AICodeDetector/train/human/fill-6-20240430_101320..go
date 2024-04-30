// Package ftp implements a FTP client as described in RFC 959.
//
// A textproto.Error is returned for errors at the FTP server.
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
	// The default initial FTP connection timeout was chosen as it's the
	// same duration of the FTP connection timeout.
	DefaultDialTimeout = 30 * time.Second
)

// EntryType describes the different types of an Entry.
type EntryType int

// The differents types of an Entry
const (
	EntryTypeFile EntryType = iota
	EntryTypeFolder
	EntryTypeLink
)

// TransferType describes the formats for transferring Entries.
type TransferType string

// FTP transfer types
const (
	TransferTypeBinary = TransferType("I")
	TransferTypeASCII  = TransferType("C")
)

// Time format used by the RFC
const MFMT DateTime = "20060102150405"

// ServerConn represents the connection to a remote FTP server.
// A single connection only supports one in-flight data connection.
// It is not safe to be called concurrently.
type ServerConn struct {
	options *dialOptions
	conn    *textproto.Conn // connection