fetch("https://brasilapi.com.br/api/ibge/uf/v1")
    .then(response => response.json())
    .then(data => {

        data.sort((a, b) => {
            const siglaA = a.sigla.toUpperCase();
            const siglaB = b.sigla.toUpperCase();

            if (siglaA < siglaB) {
                return -1;
            }
            if (siglaA > siglaB) {
                return 1;
            }
            return 0;
        });

        preencherDataListUF(data);
        preencherDataListUFB(data);
    })
    .catch(error => console.error('Erro: ', error));


function preencherDataListUF(data) {
    const datalistElement = document.getElementById('listaDeUfs')

    data.forEach(item => {
        const option = document.createElement('option');
        option.value = item.sigla;
        option.text = item.sigla;
        datalistElement.appendChild(option);
    });
}

document.getElementById('UfPontaA').addEventListener('input', () => {
    const ufInput = document.getElementById('UfPontaA');
    const cidadeDataList = document.getElementById('listaDeCidades');
    const ufSelecionada = ufInput.value;

    preencherCidadesDatalist(ufSelecionada)
    obterDadosParaLatLong(ufSelecionada)
});

function preencherCidadesDatalist(ufSelecionada) {
    const novaURL = `https://brasilapi.com.br/api/ibge/municipios/v1/${ufSelecionada}?providers=dados-abertos-br,gov,wikipedia`;

    fetch(novaURL)
        .then(response => response.json())
        .then(data => {
            const cidadeDataList = document.getElementById('listaDeCidades');
            cidadeDataList.innerHTML = '';

            data.forEach(cidade => {
                const option = document.createElement('option');
                option.value = cidade.nome;
                cidadeDataList.appendChild(option);
            });
    })
    .catch(error => console.error('Erro ao preencher cidades: ', error));
}

document.getElementById('CidadePontaA').addEventListener('inout', () => {
    const cidadeInput = document.getElementById('CidadePontaA');
    const cidadeSelecionada = cidadeInput.value;
});

function preencherDataListUFB(data) {
    const datalistElement = document.getElementById('listaDeUfsB')

    data.forEach(item => {
        const option = document.createElement('option');
        option.value = item.sigla;
        option.text = item.sigla;
        datalistElement.appendChild(option);
    });
}

document.getElementById('UfPontaB').addEventListener('input', () => {
    const ufInput = document.getElementById('UfPontaB');
    const cidadeDataList = document.getElementById('listaDeCidadesB');
    const ufSelecionada = ufInput.value;

    preencherCidadesDatalistB(ufSelecionada)
});

function preencherCidadesDatalistB(ufSelecionada) {
    const novaURL = `https://brasilapi.com.br/api/ibge/municipios/v1/${ufSelecionada}?providers=dados-abertos-br,gov,wikipedia`;

    fetch(novaURL)
        .then(response => response.json())
        .then(data => {
            const cidadeDataList = document.getElementById('listaDeCidadesB');
            cidadeDataList.innerHTML = '';

            data.forEach(cidade => {
                const option = document.createElement('option');
                option.value = cidade.nome;
                cidadeDataList.appendChild(option);
            });
    })
    .catch(error => console.error('Erro ao preencher cidades: ', error));
}

/*
document.addEventListener('DOMContentLoaded', fetchData);

function fetchData() {
    const dataTable = document.getElementById('data-table');
    const dataBody = document.getElementById('data-body');

    const apiUrl = 'http://127.0.0.1:5000/rotas_backbone';

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            const row = dataBody.insertRow();
            const columns = [
                item.nome,
                item.descricao,
                item.uf_ponta_a,
                item.cidade_ponta_a,
                item.uf_ponta_b,
                item.cidade_ponta_b,
                createEditButton(),
                createDeleteButton()
            ];

            columns.forEach((column, index) => {
                const cell = row.insertCell(index);
                cell.textContent = column;
            });
        });
    })
    .catch(error => {
        console.error('Ocorreu um erro ao buscar os dados da API:', error);
    });
}

function createEditButton() {
    const editButton = document.createElement('button');
    editButton.textContent = 'Editar';
    editButton.addEventListener('click', () => {
        alert('Editar');
    });
    return editButton;
}

function createDeleteButton() {
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Deletar';
    deleteButton.addEventListener('click', () => {
        // Lógica para deletar a linha aqui
        alert('Deletar: Implemente a lógica de exclusão aqui');
    });
    return deleteButton;
}
*/

fetch('http://127.0.0.1:5000/rotas_backbone')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            const id = item.id;
            const nome = item.nome;
            const descricao = item.descricao;
            const uf_ponta_a = item.uf_ponta_a;
            const cidade_ponta_a = item.cidade_ponta_a;
            const uf_ponta_b = item.uf_ponta_b;
            const cidade_ponta_b = item.cidade_ponta_b;
        });

        preencherListaDeRotasBackbone(data);
    })
    .catch(error => console.error('Erro: ', error));

function preencherListaDeRotasBackbone(data) {
    const tableElement = document.getElementById('data-body')

    data.forEach((item) => {
        const tr = document.createElement('tr');
    });
}

    const datalistElement = document.getElementById('listaDeUfs')

    data.forEach(item => {
        const option = document.createElement('option');
        option.value = item.sigla;
        option.text = item.sigla;
        datalistElement.appendChild(option);
    });
