// cep.js

// Aplicar máscara de entrada aos campos de CEP e telefone
document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('id_zip_code');
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
    const cep = document.getElementById('id_zip_code').value.replace('-', '');
    const cepError = document.getElementById('cep-error');

    // if (!validarCEP(cep)) {
    //     cepError.style.display = 'block';
    //     return;
    // } else {
    //     cepError.style.display = 'none';
    // }

    document.getElementById('id_address').value = "";
    document.getElementById('id_number').value = "";
    document.getElementById('id_complement').value = "";
    document.getElementById('id_district').value = "";
    document.getElementById('id_city').value = "";
    document.getElementById('id_state').value = "";
    document.getElementById('id_ibge_code').value = "";
    document.getElementById('id_gia_code').value = "";
    document.getElementById('id_ddd_code').value = "";
    document.getElementById('id_siafi_code').value = "";

    const url = `https://viacep.com.br/ws/${cep}/json/`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Erro ao buscar o CEP');
            window.alert('CEP não existe ou informado errado, verificar!')
        }

        const data = await response.json();
        if (data.erro) {
            throw new Error('CEP não encontrado');
            window.alert('CEP não existe ou informado errado, verificar!')
        }

        document.getElementById('id_address').value = data.logradouro;
        document.getElementById('id_district').value = data.bairro;
        document.getElementById('id_city').value = data.localidade;
        document.getElementById('id_state').value = data.uf;
        document.getElementById('id_ibge_code').value = data.ibge;
        document.getElementById('id_gia_code').value = data.gia;
        document.getElementById('id_ddd_code').value = data.ddd;
        document.getElementById('id_siafi_code').value = data.siafi;
    } catch (error) {
        alert(error.message);
    }
}