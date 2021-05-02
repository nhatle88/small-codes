Terminal: heroku login
Terminal: heroku apps: create <your-app>
Terminal: cd <your-project>
Terminal: touch index.php
Open file index.php to add this code below
<?php header( 'Location: /index.html' ) ;  ?>
Terminal: git init
Terminal: git add .
Terminal: git commit -m "your-comment"
Terminal: git push heroku master
