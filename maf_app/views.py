from django.shortcuts import render



def maf(request):
	return render(request, 'maf_app/maf.html', {})

def femicidios_list(request):
	return render(request, 'maf_app/maf.html', {})

