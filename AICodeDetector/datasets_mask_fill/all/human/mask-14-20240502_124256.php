<?php
// 複数の受信者を指定
$to = 'johny@example.com, sally@example.com'; // カンマに注意

// 表題
$subject = 'Birthday Reminders for August';

// 本文
$message = <extra_id_0> <title>Birthday Reminders for August</title>
</head>
<body>
  <p>Here are the birthdays upcoming in August!</p>
  <table>
    <tr>
   <extra_id_1>  <th>Person</th><th>Day</th><th>Month</th><th>Year</th>
    </tr>
    <extra_id_2>     <td>Johny</td><td>10th</td><td>August</td><td>1970</td>
    </tr>
    <tr>
 <extra_id_3>    <td>Sally</td><td>17th</td><td>August</td><td>1973</td>
    <extra_id_4> </table>
</body>
</html>
';

// HTML メールを送信するには Content-type ヘッダが必須
$headers[] = 'MIME-Version: 1.0';
$headers[] <extra_id_5> text/html; charset=iso-8859-1';

// 追加のヘッダ
$headers[] = 'To: Mary <mary@example.com>, <extra_id_6> = 'From: Birthday Reminder <birthday@example.com>';
$headers[] = 'Cc: birthdayarchive@example.com';
$headers[] = 'Bcc: <extra_id_7> $subject, $message, implode("\r\n", $headers));
?>
