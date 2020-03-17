# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
import csv
from .models import Seguimiento
from datetime import datetime



def index(request):

	Seguimiento.objects.all().delete()



	## Loading data....
	with open('data_source.csv', 'r') as file:
		data = csv.reader(file)

		for row in data:
			reg = Seguimiento()
			reg.proyecto = row[0]
			reg.etapa = row[1]
			reg.sector = row[2]
			reg.unidad = row[3]
			reg.cliente = row[4]
			try:
				reg.finspeccion = datetime.strptime(row[5], '%d/%m/%Y')
			except:
				reg.finspeccion = None
			
			try:
				reg.frmunicipal = datetime.strptime(row[6], '%d/%m/%Y')
			except:
				reg.frmunicipal = None
			
			try:
				reg.fvconstructor = datetime.strptime(row[7], '%d/%m/%Y')
			except: 
				reg.fvconstructor =None
			reg.dias = row[8]
			reg.estado =row[9]
			reg.save()
	headers = ['Proyecto','Etapa','Sector','Unidad', 'Cliente', 'F.Inspección', 'F.R. Municipal', 'F.V. Constructor', 'Dias', 'Estado']
	registros = Seguimiento.objects.all().values()
	print("Estos son los registros....")
	print(registros)
	context = {
    			'headers': headers, 
                'registros': registros,
                }



	return render(request, 'index.html', context)

#class HomeView(TemplateView):
 #   template_name = 'index.html'