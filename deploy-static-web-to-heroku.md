Terminal: heroku login <br>
Terminal: heroku apps: create <your-app> <br>
Terminal: cd <your-project> <br>
Terminal: touch index.php <br>
Open file index.php to add this code below <br>
<?php header( 'Location: /index.html' ) ;  ?>
Terminal: git init <br>
Terminal: git add .<br>
Terminal: git commit -m "your-comment"<br>
Terminal: git push heroku master<br>
