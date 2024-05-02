

use Symfony\Contracts\HttpClient\HttpClientInterface;
use Symfony\Contracts\HttpClient\HttpClient;

// Symfony以外の場合
$client = HttpClient::create();
$response = $client->request('GET', 'https://qiita.com/api/v2/items?query=Symfony', [
    'headers' => [
        'Authorization' => 'Bear: ......'
    ],
]);

// ステータスコード
$statusCode = $response->getStatusCode();
// レスポンスヘッダ
$headers = $response->getHeaders();
// レスポンスを文字列で
$response->getContent();
// レスポンスを配列で
$response->toArray();

// Symfonyの場合
class SomeService
{
    public function __construct(private readonly HttpClientInterface $client)
    {
    }
    
    public function someMethod()
    {
        $response = $client->request('GET', 'https://qiita.com/api/v2/items?query=Symfony', [
            'headers' => [
                'Authorization' => 'Bear: ......'
            ],
        ]);
        
        // 以下同様
    }
}
