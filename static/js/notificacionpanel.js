NOTIFICACION_ALERTA = 1;
NOTIFICACION_ERROR = 2;
NOTIFICACION_INFO = 3;

function defaultFor(arg, val) { return typeof arg !== 'undefined' ? arg : val; }

iconoNotificacion = function(t) {
    if (t==NOTIFICACION_ALERTA) {
        return "<img src='/static/img/dalerta.png' alt='ALERTA' width='50px'/>";
    } else if (t==NOTIFICACION_ERROR) {
        return "<img src='/static/img/derror.png' alt='ERROR' width='50px'/>";
    } else if (t==NOTIFICACION_INFO) {
        return "<img src='/static/img/dinfo.png' alt='INFO' width='50px'/>";
    }
};

notificarError = function(titulo, mensaje, boton, fboton) {
    mostrarNotificacionPanel(NOTIFICACION_ERROR, titulo, mensaje, boton1='', fboton1=null, boton2=boton, fboton2=fboton);
};

notificarAlerta = function(titulo, mensaje, boton, fboton) {
    mostrarNotificacionPanel(NOTIFICACION_ALERTA, titulo, mensaje, boton1='', fboton1=null, boton2=boton, fboton2=fboton);
};

notificarInfo = function(titulo, mensaje, boton, fboton) {
    mostrarNotificacionPanel(NOTIFICACION_INFO, titulo, mensaje, boton1='', fboton1=null, boton2=boton, fboton2=fboton);
};

mostrarNotificacionPanel = function(tipo, titulo, mensaje, boton1, fboton1, boton2, fboton2) {

    boton2 = defaultFor(boton2, "");
    boton1 = defaultFor(boton1, "");

    $("#notificacionpanel .paneltitle").html(titulo);
    $("#notificacionpanel .panelbody").html("<table><tr><td width='60px'>"+iconoNotificacion(tipo)+"</td><td valign='top'>"+mensaje+"</td></tr></table>");
    if (boton1.length>0) {
        $("#notificacionpanel .boton1").html(boton1);
        $("#notificacionpanel .boton1").unbind("click").click(fboton1).show();
    } else {
        $("#notificacionpanel .boton1").unbind("click").hide();
    }
    if (boton2.length>0) {
        $("#notificacionpanel .boton2").html(boton2);
        $("#notificacionpanel .boton2").unbind("click").click(fboton2).show();
    } else {
        $("#notificacionpanel .boton2").unbind("click").hide();
    }

    $("#notificacionpanel").modal({backdrop: 'static', keyboard: false});
    $("#notificacionpanel .ajaxlink").click(function() {
        var linked = $(this).attr("linked");
        $.get(linked,{}, function() {

        },"json");
        return false;
    });
    $("#notificacionpanel").modal("show");

};

cerrarNotificacionPanel = function() {
    $("#notificacionpanel").modal("hide");
    return false;
};