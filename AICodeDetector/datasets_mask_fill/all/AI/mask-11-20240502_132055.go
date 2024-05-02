import (
  <extra_id_0> "io/ioutil"
    "net/http"
)

func httpGet(url string) (string, error) <extra_id_1>   resp, err := http.Get(url)
    <extra_id_2> != nil {
   <extra_id_3>    return "", err
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
     <extra_id_4>  return "", err
    }
    <extra_id_5> nil
}
