// Aqui van las funciones para modificar el DOM cuando 
// se llamen las funciones de python

function crear_despachador() {
	py_despachador(js_mostrar_info_micro);
}

function js_mostrar_info_micro(id_micro, string_datos) {
	var html = `<h1>Micro ${id_micro}</h1>`;

	html += `
		<table class="table table-dark table-striped">
		<thead>
                <tr>
                    <th>Disponible</th>
                    <th>Proceso</th>
                    <th>TCC</th>
                    <th>TE</th>
                    <th>TVC</th>
                    <th>TB</th>
                    <th>TT</th>
                    <th>TI</th>
                    <th>TF</th>
                </tr>
            </thead>
		<tbody>
	`;

	var string_filas = string_datos.split("#");
	const filas = string_filas.values();
	for (const valorf of filas) {
		var string_columnas = valorf.split(",");
		const columnas = string_columnas.values();
		var dato = []
		var contador = 0;

		for (const valorc of columnas) {
			dato[contador] = valorc;
			contador += 1;
		}

		html += 
		`
			<tr>
                <td>${dato[0]}</td>
                <th scope="row">${dato[1]}</th>
                <td>${dato[2]}</td>
                <td>${dato[3]}</td>
                <td>${dato[4]}</td>
                <td>${dato[5]}</td>
                <td>${dato[6]}</td>
                <td>${dato[7]}</td>
                <td>${dato[8]}</td>
            </tr>
		`;
	}

	html += `
		</tbody>
		</table>
	`;

	document.getElementById("contenido").innerHTML += html;
}