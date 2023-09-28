/*
  ----------------------------------------------------------------
    Função para obter lista de UFs vindo da API Externa
  ----------------------------------------------------------------
*/

const obterListaDeUFs = async () => {

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
}


obterListaDeUFs()

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


const obterDadosDasRotasCadastradas = async () => {

    const dataList = document.getElementById('data-list');
    dataList.innerHTML = ''; // Limpa a lista antes de adicionar novos elementos

    let url = "http://127.0.0.1:5000/rotas_backbone";

    fetch(url, {method: 'get'})
    .then(response => response.json())
    .then(data => {

        data.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `Nome: ${item.nome}, Descrição: ${item.descricao}`;
            dataList.appendChild(listItem);
        });

})
.catch(error => console.error('Erro: ', error));
}

obterDadosDasRotasCadastradas();