// Package ftp implements a FTP client as described in RFC 959.
//
// A textproto.Error is returned for errors at the <extra_id_0> ftp

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
	// <extra_id_1> was chosen as it's the
	// same duration <extra_id_2> timeout.
	DefaultDialTimeout = 30 * time.Second
)

// EntryType describes the different types of an Entry.
type <extra_id_3> The differents types of an Entry
const (
	EntryTypeFile EntryType = iota
	EntryTypeFolder
	EntryTypeLink
)

// <extra_id_4> the formats for transferring Entries.
type TransferType string

// <extra_id_5> transfer types
const (
	TransferTypeBinary = TransferType("I")
	TransferTypeASCII  <extra_id_6> Time format used by the <extra_id_7> MFMT <extra_id_8> = "20060102150405"

// ServerConn represents the connection to a remote FTP server.
// A single connection only supports one in-flight data connection.
// It is not safe to be called concurrently.
type ServerConn struct {
	options *dialOptions
	conn    *textproto.Conn // connection