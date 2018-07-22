from django.test import TestCase

# Create your tests here.
	{% if forloop.first %}
 			<p>{{k}}</p>
 		{% endif %}

{% for k in i %}
 		<p>{{i.title}}</p>
 		
 		
 	
 	{% endfor %}