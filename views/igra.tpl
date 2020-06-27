% import model
%rebase('base.tpl', title='Vislice')

<table>

<tr>

    <td>

        <h2>{{igra.pravilni_del_gesla()}}</h2>

    </td>

</tr>

<tr>

    <td>

        <br> Nepravilni ugibi : {{igra.nepravilni_ugibi()}}

    </td>

</tr>

<tr>

    <td>

        <img src="../img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

    </td>

</tr>

</table>



% if poskus == model.ZMAGA:



<h1>ZMAGA! ČESTITKE! ;)</h1>



<form action="/igra/" method="post">

    <button type="submit">Nova igra</button>

</form>



% elif poskus == model.PORAZ:



<h1>KONEC! IZGUBIL SI!</h1>



Pravilno geslo: {{igra.geslo}}



<form action="/igra/" method="post">

    <button type="submit">Nova igra</button>

</form>



% else:



<form action="/igra/{{id_igre}}/" method="post">

    Črka: <input type="text" name="crka" autofocus>

    <button type="submit">Pošlji ugib</button>

</form>

% end
#popravi