 var uniqueId = function () {
   return '_' + Math.random().toString(36).substr(2, 9);
};

var isComponentType = function (component, componentType) {
    const typeString = get(component, 'type', '').toString()
    const componentTypeString = componentType.toString()
    return _.isEqual(typeString, componentTypeString)
}

var stringifyOptions = function (obj) {
   return _.replace(stringify(obj), /"/g, `'`)
}

var options = function (str) {
   return JSON.parse(String(str).replace(/'/g,"\""));
};

var callMethod = function (methodName, params) {
  return `javascript:window.${methodName}(${map(params, (item) => {
    if (typeof item === 'string') {
      return "'" + item + "'"
    } else if (typeof item === 'number') {
      return item
    }
    return item
  }).join(',')})`
}

var dataBind = function (name, bindFunc) {
    const $elem = $(`[data-zhiyu-${name}]`);
    $elem.each((index, item) => {
    const $item = $(item)
    const result = $item.data(`zhiyu-${name}-result`)
    if(result !== 'success'){
        const option = $(item).data(`zhiyu-${name}`);
        bindFunc($(item), option, index)
        $item.data(`zhiyu-${name}-result`,'success')
   }
 })
};

// 绑定对话框按钮
var bindModalAction = function ($elem, callback) {
  const confirmBtn = $elem.find('[data-confirm]')
  const cancelBtn = $elem.find('[data-cancel]')
  const onDismiss = () => {
    $elem.modal('hide')
  }
  if (confirmBtn) {
    $(confirmBtn).on('click', () => {
      let isDismiss
      if (callback && callback.confirm) {
        isDismiss = callback.confirm(onDismiss)
      }
      if (isDismiss === undefined || isDismiss === true) {
        onDismiss()
      }
    })
  }
  if (cancelBtn) {
    $(cancelBtn).on('click', () => {
      let isDismiss
      if (callback && callback.cancel) {
        isDismiss = callback.cancel(onDismiss)
      }
      if (isDismiss === undefined || isDismiss === true) {
        onDismiss()
      }
    })
  }
};

var showDialog = function ({title, content, footer, shownCallback, hiddenCallback, actionCallback, modalOptions}) {
    var html ="";
    html += `
   <div class="modal fade" tabIndex="-1" role="dialog" aria-labelledby="gridSystemModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close" onClick="onCancel">
            <span aria-hidden="true">&times;</span>
          </button>
          <h4 class="modal-title" id="gridSystemModalLabel">${title}</h4>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-12">${content}</div>
          </div>
        </div>`;
        if (footer === undefined || footer === ""){
            html += `<div class="modal-footer">
            <button type="button" class="btn btn-default" data-cancel>取消</button>
            <button type="button" class="btn btn-primary" data-confirm>确定</button>
          </div>`
        } else {
            html += footer;
        }
       html += `
      </div>
    </div>
  </div>
  `
var $modal = $(html);
  var $body = $('body');
  $body.append($modal);
  $modal.modal(modalOptions);
  $modal.on('shown.bs.modal', function (e) {
    shownCallback && shownCallback($modal, e)
  });

  $modal.on('hidden.bs.modal', function (e) {
    hiddenCallback && hiddenCallback($modal, e)
    $modal.remove()
  });
  bindModalAction($modal, actionCallback)
};

var confirm = function ({message, callback}) {
  showDialog({
    title: '提示',
    content: (
        `
        <div class="pl-4 pr-4">
            <div class="text-left">
              ${message}
            </div>
        </div>`
    ),
    shownCallback($modal) {
      bindModalAction($modal, callback)
    }
  })
};
