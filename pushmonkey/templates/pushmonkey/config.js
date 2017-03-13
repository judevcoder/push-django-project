{% if not is_demo %}
window.onload = function() {
{% endif %}

    try {
        window.pushMonkeyConfig = {
            accountKey: "{{ account_key }}",
            dialogColor: "{{ dialog_color }}",
            dialogButtonColor: "{{ button_color }}",
            isNotWordpress: {{ is_not_wordpress }},
            {% if account_key == "LGD5MFJ4Q6CPKI3RH" %}
            segmentation: 1,
            debug: 1
            {% else %}
            segmentation: 0,
            debug: 0
            {% endif %}
        }
        var container = document.body ? document.body : document.head;
        var script = document.createElement("script");
        script.id = "PushMonkeySDK";
        {% if account_key == "LGD5MFJ4Q6CPKI3RH" %}
        script.src = "/sdk/sdk-{{ account_key }}.js";
        {% else %}
        script.src="//www.getpushmonkey.com/sdk/sdk-{{ account_key }}.js";
        {% endif %}
        container.appendChild(script);
    } catch(err) {
    }
{% if not is_demo %}    
};
{% endif %}