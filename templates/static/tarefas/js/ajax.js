$(document).ready(function() {
  // Capture o evento de alteração do checkbox
  $('.checkbox').change(function() {
    // Obtenha o ID do modelo a ser atualizado
    var tarefa_id = $(this).attr('id').split('_')[1];
    
    // Obtenha o estado atual do checkbox
    var status = $(this).is(':checked') ? 'C' : 'N';

    // Envie a requisição Ajax para atualizar o modelo
    $.ajax({
        url: 'atualizar_tarefa/',
        type: 'POST',
        data: {
            tarefa_id: tarefa_id,
            status: status
        },
        success: function(response) {
          console.log(response.mensagem);
        },
        error: function(response) {
          console.log(response.erro);
        }
    });
  });
});

$(document).ready(function() {
  $('.checkbox').on('change', function() {
    var id = $(this).attr('id').replace('check_', '');
    var spanElement = $('#span_' + id);
    var divElement = $('#div_' + id);
    
    if ($(this).is(':checked')) {
      spanElement.addClass('marked');
      divElement.addClass('bg-tranparent');
    } else {
      spanElement.removeClass('marked');
      divElement.removeClass('bg-tranparent');
    }
  });
});

