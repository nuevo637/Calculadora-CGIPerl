#!"C:/xampp/perl/bin/perl.exe"
use CGI;

my $cgi = CGI->new;

print $cgi->header('text/html');
my $operacion = $cgi->param('operacion');

print "<html><body>";
print "<h1>Texto Recibido:</h1>";
print "<p>$operacion</p>";
print "</body></html>";