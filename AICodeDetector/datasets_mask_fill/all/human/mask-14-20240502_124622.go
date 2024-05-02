package <extra_id_0>    "fmt"
  <extra_id_1> "io"
    "os"
    "net"
  <extra_id_2> "net/url"
    "bufio"
    "strings"
    <extra_id_3>   "golang.org/x/crypto/ssh"
    "golang.org/x/crypto/ssh/agent"

    "github.com/pkg/sftp"
)

func main() <extra_id_4>   // Get <extra_id_5> Go URL from environment
    rawurl := os.Getenv("SFTPTOGO_URL")

 <extra_id_6>  parsedUrl, err := url.Parse(rawurl)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Failed to parse SFTP To <extra_id_7> %s\n", err)
        os.Exit(1)
    }

    // Get user name and pass
    user := parsedUrl.User.Username()
 <extra_id_8> 