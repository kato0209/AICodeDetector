<?php

declare(strict_types=1);

require_once('vendor/autoload.php');

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

const <extra_id_0> 'https://api.flickr.com/services';
const PHOTO_URL <extra_id_1> PHOTOS_DIR = 'photos';

$apiKey=$_ENV['API_KEY'];

$opts <extra_id_2>    'https' => [
        <extra_id_3> 3,
    <extra_id_4> http_build_query([
    'api_key' => $apiKey,
    'content_type' => 1,
    'format' => 'php_serial',
    'media' => 'photos',
   <extra_id_5> => 'flickr.photos.search',
    'per_page' => 10,
    'safe_search' => 1,
    'text' => 'Kakadu National Park'
]);
$requestUri = sprintf(
    '%s/rest/?%s',
  <extra_id_6> BASE_URL,
    <extra_id_7> fopen($requestUri, 'r');

$photoData = unserialize(stream_get_contents($fp));

foreach ($photoData['photos']['photo'] as $photoDatum) {
    printf("Downloading <extra_id_8>    $photoFile = file_get_contents(
       