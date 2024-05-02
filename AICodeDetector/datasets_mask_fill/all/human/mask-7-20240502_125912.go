// Package ftp implements a FTP client <extra_id_0> in RFC 959.
//
// A <extra_id_1> returned for errors at the protocol level.
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

// EntryType describes the different <extra_id_2> an <extra_id_3> int

// The differents types of an Entry
const (
	EntryTypeFile EntryType = iota
	EntryTypeFolder
	EntryTypeLink
)

// TransferType <extra_id_4> formats for transferring Entries.
type TransferType string

// The different transfer types
const (
	TransferTypeBinary = TransferType("I")
	TransferTypeASCII  = TransferType("A")
)

// Time format used by the MDTM and MFMT commands
const timeFormat = "20060102150405"

// ServerConn represents the connection to a remote FTP server.
// A single connection only <extra_id_5> in-flight data <extra_id_6> is not safe to be called concurrently.
type <extra_id_7> {
	options *dialOptions
	conn    <extra_id_8> connection