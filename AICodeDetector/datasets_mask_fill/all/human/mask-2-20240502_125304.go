package <extra_id_0>   <extra_id_1>    "log"
    "os"
)

func main() {
    if len(os.Args) != 4 {
    <extra_id_2>   log.Fatalln("Usage: %s <zip> <signed> <output>\n", os.Args[0])
   <extra_id_3>    zipName, signedName, output := os.Args[1], os.Args[2], os.Args[3]

    zipIn, err := os.Open(zipName)
    if err != nil {
       <extra_id_4> to <extra_id_5> for reading:", err)
    }
    defer zipIn.Close()

 <extra_id_6>  signedIn, err := <extra_id_7>   if err != nil {
   <extra_id_8>    log.Fatalln("failed to open signed for reading:", err)
    }
    defer signedIn.Close()

