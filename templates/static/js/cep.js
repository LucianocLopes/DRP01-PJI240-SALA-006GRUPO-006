function buscarCep() {
    const cep = document.getElementById('cep').value;
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = '';  // Limpa mensagens de erro anteriores

    // Valida o CEP (apenas números e tamanho 8)
    const validCep = /^[0-9]{8}$/;
    if (!validCep.test(cep)) {
        errorMessage.textContent = 'CEP inválido. Digite 8 números.';
        return;
    }

    // URL da API ViaCEP
    const url = `https://viacep.com.br/ws/${cep}/json/`;

    // Faz a requisição para a API ViaCEP
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao buscar o CEP. Verifique se o CEP está correto.');
            }
            return response.json();
        })
        .then(data => {
            if (data.erro) {
                throw new Error('CEP não encontrado.');
            }

            // Preenche os campos do formulário com os dados recebidos
            document.getElementById('logradouro').value = data.logradouro || '';
            document.getElementById('bairro').value = data.bairro || '';
            document.getElementById('localidade').value = data.localidade || '';
            document.getElementById('uf').value = data.uf || '';
        })
        .catch(error => {
            errorMessage.textContent = error.message;
            // Limpa os campos em caso de erro
            document.getElementById('logradouro').value = '';
            document.getElementById('bairro').value = '';
            document.getElementById('localidade').value = '';
            document.getElementById('uf').value = '';
        });
}

function validarFormulario(event) {
    const cep = document.getElementById('cep').value;
    const errorMessage = document.getElementById('error-message');
    const validCep = /^[0-9]{8}$/;

    if (!validCep.test(cep)) {
        errorMessage.textContent = 'CEP inválido. Digite 8 números.';
        event.preventDefault();  // Impede o envio do formulário
    }
}