<!DOCTYPE html>
<html>
<head>
	<title>Crime News Updates</title>
</head>
<body>
	FORM
	<form action="insert_data.php" style="border: solid; padding: 5px 5px 5px 5px" method="post">
		
		First Name: <input type="text" name="first_name"><br><br>
		Last Name: <input type="text" name="last_name"><br><br>
		Fathers Name: <input type="text" name="fathers_name"><br><br>
		gender: 
			<select name="gender" value="select">
			  <option value="select">Select</option>
			  <option value="Male">Male</option>
			  <option value="Female">Female</option>
			</select>
			<br><br>
		DOB : <input type="date" name="dob"><br><br>
		Marital Status : 
			<select name="marital_status" value="select">
			  <option value="select">Select</option>
			  <option value="Unmarried">Unmarried</option>
			  <option value="Married">Married</option>
			  <option value="Widow">Widow</option>
			  <option value="Widower">Widower</option>
			  <option value="Divorced">Divorced</option>
			</select>
			<br><br>
		Spouse Name : <input type="text" name="spouse_name"><br><br>
		Blood Group : 
			<select name="blood_group" value="select">
			  <option value="select">Select</option>
			  <option value="A+">A+</option>
			  <option value="A-">A-</option>
			  <option value="B+">B+</option>
			  <option value="B-">B-</option>
			  <option value="AB+">AB+</option>
			  <option value="AB-">AB-</option>
			  <option value="O+">O+</option>
			  <option value="O-">O-</option>
			  <option value="Others">Others</option>
			</select>
			<br><br>
		Qualification : <input type="text" name="qualification"><br><br>
		Profession : <input type="text" name="profession"><br><br>
		Mobile Number : <input type="text" name="mobile_number"><br><br>

		<input type="submit" name="submit">

	</form>

</body>
</html>