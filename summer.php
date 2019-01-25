<?php
		$servername = "localhost";
		$username = "root";
		$password = "";
		$dbname = "crime";

		// Create connection
		$conn = new mysqli($servername, $username, $password, $dbname);
		// Check connection
		if ($conn->connect_error) {
		    die("Connection failed: " . $conn->connect_error);
		} 
		else{

			echo "Connection established";
		}
		session_start();

		$sql = "SELECT ArticleId, ArticleTitle, ArticleText, ArticleDate, ArticleUrl FROM articles WHERE ArticleId=88 LIMIT 1";

		$results = $conn->query($sql);

		$rowCount = $results->num_rows;
		// $state_code = 0;
		$text = "";
	    if($rowCount > 0){

	        $row = $results->fetch_assoc();
	        echo "<br>".$row['ArticleId'];
	        echo "<br>".$row['ArticleTitle'];
	        echo "<br>".$row['ArticleText'];
	        echo "<br>".$row['ArticleDate'];
	        echo "<br>".$row['ArticleUrl'];
	        $_SESSION['id'] = $row['ArticleId'];
	        $_SESSION['title'] = $row['ArticleTitle'];
	        $_SESSION['news_text'] = $row['ArticleText'];
	        $_SESSION['date'] = $row['ArticleDate'];
	        $_SESSION['url'] = $row['ArticleUrl'];
	        $text = $row['ArticleTitle'];
	        $text .= " ";
	        $text .= $row['ArticleText'];
	    }else{
	        echo 'NO Results';
	    }

	    $row = shell_exec('E:\project\CrimeAnalysis\Scripts\activate & python E:\project\CrimeAnalysis\Scripts\loc.py "'.$text.'"');
		echo"success<br>";

		$exploded = explode(";",$row);


		echo '<form method="post" action="insert_crime.php" style="border:solid;padding: 5px 5px 5px 5px;">';
		echo '<table border="1">';

		function validate_alphanumeric_underscore($str) 
		{
		    return preg_match('/^[a-zA-Z0-9_]+$/',$str);
		}
		$count = 0;

		foreach($exploded as $var) { 
			# code...
			$entity = "";
			if($count === 0){
				$entity = "Name";
				$_SESSION['names'] = $var;
			}
			elseif ($count === 1) {
				# code...
				$entity = "Non-Crime Location";
				$_SESSION['ncl'] = $var;
			}
			elseif ($count === 2) {
				# code...
				$entity = "Crime Location";
				$_SESSION['cl'] = $var;
			}
			elseif ($count === 3) {
				# code...
				$entity = "Crime Word List";
				$_SESSION['cwl'] = $var;
			}
			$count += 1;

			echo 	'<tr>
						<th> '.$entity.' </th>
						<th> Yes </th>
						<th> No </th>
					</tr>';
			$sep = explode(' ', $var); 
			foreach ($sep as $key) {
				# code...

				if(!validate_alphanumeric_underscore($key)){
					continue;
				}
				echo 	'<tr>
							<td>'.$key.'</td>
							<td> <input type="radio" value="yes" name="'.$key.'" checked="checked"> YES </td>
							<td> <input type="radio" value="no" name="'.$key.'" > No </td>
						</tr>';
			}
			// echo $exploded[$i]."<br>";
		}
		echo "</table>";
		echo '<br>Extra names: <textarea rows="4" cols="50" name="extra_names"></textarea><br><br>';
		echo '<br>Extra non-crime-location: <textarea rows="4" cols="50" name="extra_ncl"></textarea><br><br>';
		echo '<br>Extra crime-location: <textarea rows="4" cols="50" name="extra_cl"></textarea><br><br>';
		echo '<br>Extra crime-list: <textarea rows="4" cols="50" name="extra_cwl"></textarea><br><br>';
		echo '<input type="submit">';
		echo '</form>';

		
		$conn->close();
	?>