// cep.js

// Aplicar máscara de entrada aos campos de CEP e telefone
document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('cep');
    Inputmask({ mask: '99999-999' }).mask(cepInput);

    const telefoneInput = document.getElementById('telefone');
    Inputmask({ mask: '(99) 99999-9999' }).mask(telefoneInput);
});

function validarCEP(cep) {
    window.alert(cep)
    const regex = /^[0-9]{5}-[0-9]{3}$/;
    return regex.test(cep);
}

async function buscarCEP() {
    const cep = document.getElementById('cep').value.replace('-', '');
    const cepError = document.getElementById('cep-error');
    window.alert(cep)

    // if (!validarCEP(cep)) {
    //     cepError.style.display = 'block';
    //     return;
    // } else {
    //     cepError.style.display = 'none';
    // }

    const url = `https://viacep.com.br/ws/${cep}/json/`;
    window.alert(url)

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Erro ao buscar o CEP');
        }

        const data = await response.json();
        if (data.erro) {
            throw new Error('CEP não encontrado');
        }

        document.getElementById('logradouro').value = data.logradouro;
        document.getElementById('bairro').value = data.bairro;
        document.getElementById('localidade').value = data.localidade;
        document.getElementById('uf').value = data.uf;
    } catch (error) {
        alert(error.message);
    }
}