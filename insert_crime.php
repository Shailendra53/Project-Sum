<?php

	// echo $_POST['extra'];

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

	$id = $_SESSION['id'];
	$title = $_SESSION['title'];
    $news_text = $_SESSION['news_text'];
    $date = $_SESSION['date'];
    $url = $_SESSION['url'];

	function insert_name($name, $id, $conn){

		$sql = "INSERT INTO people(article_id, 
									name) 

							VALUES 	($id, '$name')";

		if ($conn->query($sql) === TRUE) {

			echo "Success";

		} else {
		    
		    echo "FAILED";
		}
	}

	function insert_crime_loc($cl, $id, $conn){

		$sql = "INSERT INTO crime_location(article_id, 
									crime_loc) 

							VALUES 	($id, '$cl')";

		if ($conn->query($sql) === TRUE) {

			echo "Success";

		} else {
		    
		    echo "FAILED";
		}
	}

	function insert_non_crime_loc($ncl, $id, $conn){

		$sql = "INSERT INTO non_crime_location(article_id, 
									non_crime_loc) 

							VALUES 	($id, '$ncl')";

		if ($conn->query($sql) === TRUE) {

			echo "Success";

		} else {
		    
		    echo "FAILED";
		}
	}

	function insert_crime_list($cwl, $id, $conn){

		$sql = "INSERT INTO crime_list(article_id, 
									crime) 

							VALUES 	($id, '$cwl')";

		if ($conn->query($sql) === TRUE) {

			echo "Success";

		} else {
		    
		    echo "FAILED";
		}
	}

	function validate_alphanumeric_underscore($str) 
	{
	    return preg_match('/^[a-zA-Z0-9_]+$/',$str);
	}

	//INSERTING NAMES.....
	$names = explode(' ', $_SESSION['names']);
	foreach ($names as $key) {
		# code...
		if(!validate_alphanumeric_underscore($key)){
			continue;
		}
		echo $_POST[$key]."<br>";
		if($_POST[$key] === "yes")
			insert_name($key, $id, $conn);
	}

	//INSERTING NON CRIME LOCATION.....
	$names = explode(' ', $_SESSION['ncl']);
	foreach ($names as $key) {
		# code...
		if(!validate_alphanumeric_underscore($key)){
			continue;
		}
		echo $_POST[$key]."<br>";
		if($_POST[$key] === "yes")
			insert_non_crime_loc($key, $id, $conn);
	}

	//INSERTING CRIME LOCATION.....
	$names = explode(' ', $_SESSION['cl']);
	foreach ($names as $key) {
		# code...
		if(!validate_alphanumeric_underscore($key)){
			continue;
		}
		echo $_POST[$key]."<br>";
		if($_POST[$key] === "yes")
			insert_crime_loc($key, $id, $conn);
	}

	//INSERTING CRIME WORD LIST.....
	$names = explode(' ', $_SESSION['cwl']);
	foreach ($names as $key) {
		# code...
		if(!validate_alphanumeric_underscore($key)){
			continue;
		}
		echo $_POST[$key]."<br>";
		if($_POST[$key] === "yes")
			insert_crime_list($key, $id, $conn);
	}

	$count = 0;
	$extra_names = $_POST['extra_names'];
	// echo $extra_names;
	$exploded_names = explode(chr(13), $extra_names);
	foreach ($exploded_names as $name) {
		# code...
		if($count > 0){
			$name = substr($name, 1);
			
		}
		$count += 1;
		if(validate_alphanumeric_underscore($name)){
			echo $name."-><br>";
			insert_name($name, $id, $conn);
		}
	}
	$count = 0;
	$extra_ncl = $_POST['extra_ncl'];
	// echo $extra_ncl;
	$exploded_ncl = explode(chr(13), $extra_ncl);
	foreach ($exploded_ncl as $ncl) {
		# code...
		if($count > 0){
			$ncl = substr($ncl, 1);
			
		}
		$count += 1;
		if(validate_alphanumeric_underscore($ncl)){
			echo $ncl."-><br>";
			insert_non_crime_loc($ncl, $id, $conn);
		}
	}
	$count = 0;
	$extra_cl = $_POST['extra_cl'];
	// echo $extra_cl;
	$exploded_cl = explode(chr(13), $extra_cl);
	foreach ($exploded_cl as $cl) {
		# code...
		if($count > 0){
			$cl = substr($cl, 1);
			
		}
		$count += 1;
		if(validate_alphanumeric_underscore($cl)){
			echo $cl."-><br>";
			insert_crime_loc($cl, $id, $conn);
		}
	}
	$count = 0;
	$extra_cwl = $_POST['extra_cwl'];
	// echo $extra_cwl;
	$exploded_cwl = explode(chr(13), $extra_cwl);
	foreach ($exploded_cwl as $cwl) {
		# code...
		if($count > 0){
			$cwl = substr($cwl, 1);
			
		}
		$count += 1;
		if(validate_alphanumeric_underscore($cwl)){
			echo $cwl."-><br>";
			insert_crime_list($cwl, $id, $conn);
		}
	}

	

	$sql = "INSERT INTO dumped(id, 
								title, 
								text,
								date,
								url) 

						VALUES 	($id,
								'$title',
								'$news_text',
								'$date',
								'$url')";

	if ($conn->query($sql) === TRUE) {

		echo '<script language="javascript">';
	    echo 'alert("Data Added Successfully"); location.href="summer.php"';
	    echo '</script>';
	} else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	    echo '<script language="javascript">';
	    echo 'alert("Data Is Wrong.....\nPlease Check the Info Provided."); location.href="summer.php"';
	    echo '</script>';
	}

	$sql = "DELETE FROM articles WHERE ArticleID = $id";

	$results = $conn->query($sql);

	$conn->close();

?>