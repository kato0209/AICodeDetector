<!-- HTMLフォーム -->
<form method="post" action="handle_form.php">
    Name: <input type="text" name="name">
    <input type="submit">
</form>

<!-- PHPでの処理 -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    echo "Hello, " . $name;
}
?>
