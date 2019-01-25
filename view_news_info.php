<!DOCTYPE html>
<html>
<head>
	<title>Crime News Updates</title>
</head>
<body>
	<form action="" method="post">
		<b>Start-Date: </b> <input type="date" name="start_date"><br><br>
		<b>End-Date: </b><input type="date" name="end_date"><br><br>
		<button type="submit">Query</button>
	</form>

	<br>
	<hr>
	
	<?php
		$servername = "localhost";
		$username = "root";
		$password = "";
		$dbname = "CrimeAnalysis";

		// Create connection
		$conn = new mysqli($servername, $username, $password, $dbname);
		// Check connection
		if ($conn->connect_error) {
		    die("Connection failed: " . $conn->connect_error);
		} 

		$start_date = $_POST['start_date'];
		$end_date = $_POST['end_date'];

		$sql = "SELECT ArticleDate, ArticleUrl, ArticleTitle FROM Articles WHERE ArticleDate BETWEEN '$start_date' AND '$end_date'";
		$result = $conn->query($sql);

		if ($result->num_rows > 0) {
		    // output data of each row
		    echo '<h3>News Details:</h3>';
		    echo '<html>
		    		<head>
		    			<style type="text/css">
		    			tr:hover {background-color: #f5f5f5;}
		    			th {    text-align: center;background-color: #f2f2f2}
		    			table {border: solid black;}
		    			</style>
		    		<body>
		    			<table border="1" width="100%" style="">
		    				<tr><th width="10%">Date</th>
		    				<th width="40%">Url</th>
		    				<th>Title</th>';

		    while($row = $result->fetch_assoc()) {
		        echo "<tr> <td>" . $row["ArticleDate"]. " </td><td><a href='news_details.php?url=".$row["ArticleUrl"]."'>" . $row["ArticleUrl"]. "</a> </td><td>" . $row["ArticleTitle"]. "</td></tr>";
		    }

		    echo '		</table>
		    		</body>
		    	</html>';
		} else {
		    echo "No results";
		}
		$conn->close();
	?>

</body>
</html>