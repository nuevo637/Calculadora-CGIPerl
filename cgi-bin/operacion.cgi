#!"C:/xampp/perl/bin/perl.exe"
use CGI;
my $cgi = CGI->new;
print $cgi->header(-type => 'text/html', -charset => 'utf-8');

my $operacion = $cgi->param('operacion');
my $resultado;

if ($operacion =~ /^(\d+)([-+*\/])(\d+)$/) {
    my $operando1 = $1;
    my $operador = $2;
    my $operando2 = $3;
    if($operador == "/" and $operando2 == 0)
        $resultado = "Indeterminado";     
    eval {
        $resultado = eval "$operando1 $operador $operando2";
    };
}

print <<"HTML";
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <style>
        body {
            margin: 0;
            background-image: url(../images/fondo.jpg);
            background-size: auto 100%;
            background-position: center;
            height: 100vh;
        }

        section {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            height: 750px;
        }

        .contenedor {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 500px;
            width: 70%;
            max-width: 700px;
            background-color: rgb(246,176,37,0.92);
            border: 10px solid rgb(255, 0, 0,0.98);
            border-radius: 40px; 
        }

        h1 {
            margin: 0;
            font-size: 30px;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            color: rgb(226, 80, 18);
            margin-bottom: 10px;
        }

        input {
            border-radius: 10px;
            width: 650px;
            height: 35px;
            margin: 15px;
            text-align: center;
            font-size: 25px;
        }

        button {
            border-radius: 15px;
            font-size: 20px;
            width: 200px;
            height: 35px;
            background-color: rgb(78, 167, 255);
            transition: transform 0.3s ease;
        }

        button:hover {
            transform: scale(1.1);
        }

        p {
            font-size: 20px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <section>
        <div class="contenedor">
            <h1>CALCULADORA</h1>
            <p>El resultado es: $resultado</p>
        </div>
    </section>
</body>
</html>
HTML