<?php

declare(strict_types=1);

require_once('vendor/autoload.php');

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

const BASE_URL = 'https://api.flickr.com/services';
const PHOTO_URL = 'https://api.flickr.com/services/photo/browse';
const PHOTOS_DIR = 'photos';

$apiKey=$_ENV['API_KEY'];

$opts = [    'https' => [
        'verify' => 3,
    ],
];
$searchQuery = http_build_query([
    'api_key' => $apiKey,
    'content_type' => 1,
    'format' => 'php_serial',
    'media' => 'photos',
   'method' => 'flickr.photos.search',
    'per_page' => 10,
    'safe_search' => 1,
    'text' => 'Kakadu National Park'
]);
$requestUri = sprintf(
    '%s/rest/?%s',
   BASE_URL,
    $searchQuery
);
$fp = fopen($requestUri, 'r');

$photoData = unserialize(stream_get_contents($fp));

foreach ($photoData['photos']['photo'] as $photoDatum) {
    printf("Downloading photo...\n");    $photoFile = file_get_contents(
       