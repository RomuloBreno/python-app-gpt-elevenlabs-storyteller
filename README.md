# Projeto de Criação de Roteiros e Narrações para Mídias Sociais

Este projeto é uma aplicação pensada e fundamentada na criação de roteiros e narrações para mídias sociais, utilizando a inteligência artificial do ChatGPT em conjunto com a ElevenLabs para geração e narração de textos. A solução visa facilitar a criação de conteúdo dinâmico e atraente para diversas plataformas.

## Funcionalidades

- **Geração de Roteiros**: Com o uso do ChatGPT, o sistema gera roteiros customizados para postagens e vídeos de acordo com os padrões de escrita definidos.
- **Narrações Automatizadas**: Integração com a API ElevenLabs para transformar os roteiros em narrações de alta qualidade.
- **Suporte Multilíngue**: Capaz de gerar conteúdos em múltiplos idiomas, aproveitando as capacidades do modelo multilingue v2 do ElevenLabs.

## Requisitos

Para que o projeto seja iniciado, certifique-se de que os seguintes requisitos sejam atendidos:

- **Python 3.11**: A aplicação foi desenvolvida utilizando Python 3.11. Certifique-se de que esta versão esteja instalada no seu ambiente.
  
  Você pode verificar sua versão do Python com o comando:
  
  ```bash
  python --version
  ```

## Configuração das Chaves de API: 
- O arquivo appsettings.json contém as chaves das APIs do ChatGPT e ElevenLabs, bem como os diretórios de trabalho. Certifique-se de substituir essas chaves pelas suas credenciais pessoais e ajustar os diretórios conforme sua necessidade.

## Modelos de Roteiros Personalizados:
- Existem dois arquivos base localizados no diretório /base/prompt/. Estes arquivos podem ser modificados para adequar o formato de roteiro desejado.
Esses arquivos servem como template para a geração de roteiros e podem ser adaptados conforme as necessidades de cada projeto.
