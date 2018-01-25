# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import Context
from django.db.models import Q
from django.db.models import Count, Min

from django.http import JsonResponse
from .forms import CommForm, comment_form
from .models import Comm_Item, comment

from django.urls import reverse_lazy, reverse

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
class TypeofView(ListView):
	context_object_name = 'inv_com'
	model = Comm_Item
	template_name = 'staffcom/frontpage.html'
	commtype = 'Inventory'


	def get_queryset(self):
		rtn_query_list = Comm_Item.objects.filter(comm_type=self.commtype, visible=True).order_by('-date', '-title').annotate(
			num_comments=Count('comments'), earliest_comment=Min('comments__date_time'))
		paginator = Paginator(rtn_query_list, 10)
		page = self.request.GET.get('page')
		try:
			rtn_query = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			rtn_query = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			rtn_query = paginator.page(paginator.num_pages)

		return rtn_query
	

	def get_context_data(self, **kwargs):
		viewname = super(TypeofView, self).get_context_data(**kwargs)
		viewname['viewname'] = self.commtype
		viewname['username'] = self.request.user.get_username()
		return viewname
			

class Inventory_View(TypeofView):
	pass
	#default type of view with only inventory view that doesn't require a login

class View_with_PHI(LoginRequiredMixin, TypeofView):
	# view that requires LOGIN
	pass


class DetailPostView(DetailView):
	context_object_name = 'post'
	template_name = 'staffcom/detail.html'
	model = Comm_Item
	def get_context_data(self, **kwargs):
		post_pk = self.kwargs['pk']
		context = super(DetailPostView, self).get_context_data(**kwargs)
		context['comments'] = Comm_Item.objects.get(pk = post_pk).comments.all().order_by('-date_time')
		return context

class UpdatePostView(LoginRequiredMixin, UpdateView):
	model = Comm_Item
	fields = ['title', 'comm_type', 'descr', 'visible']
	template_name = 'staffcom/update_post.html'

	def get_success_url(self):
		return reverse('details',kwargs={'pk' : self.kwargs.get('pk')})

	def form_valid(self, form):
		self.object.created_by = User.objects.get(username = self.request.user.get_username())
		self.object.save()
		return redirect('details', pk = self.object.id)


class DeletePostView(LoginRequiredMixin,DeleteView):
	model = Comm_Item
	success_url = reverse_lazy('inventory')


# function views below
@login_required
def form_view(request):

	comm = CommForm()	
	if request.method == 'POST':
		form = CommForm(request.POST)
		if form.is_valid():
			view = form.cleaned_data.get('comm_type')
			usn = request.user.get_username()
			form.instance.created_by=User.objects.get(username=usn)
			urls_view = {'Inventory':'inventory', 'Chemo':'chemo', 
			'Operation':'ops', 'HomeIV':'homeiv'}
			form.save(commit = True)
			return redirect(urls_view.get(view))

	return render(request, 'staffcom/newpost.html', {'form': comm})

@login_required
def comment_view(request, pk):
	if request.method == "GET":
		comm_form = comment_form()
		post_object = Comm_Item.objects.get(pk = pk)
		return render(request, 'staffcom/comment.html', {'form':comm_form, 'post':post_object})

	if request.method == 'POST':
		form = comment_form(request.POST)
		if form.is_valid():
			usn = request.user.get_username()
			new_com = comment()
			new_com.content = form.cleaned_data.get('content')
			new_com.link_to_comm = Comm_Item.objects.get(pk = pk)
			new_com.username = User.objects.get(username = usn)
			new_com.save()
			return redirect('details', pk = pk)

	return render(request, 'staffcom/comment.html', {'form': comm_form})

@login_required
def search_posts(request):
	if request.method == "GET":
		if request.is_ajax():
			query = request.GET.get('searchText')
			objects = Comm_Item.objects.filter(Q(visible = True), Q(title__contains = query)|Q(descr__contains = query)).order_by('-date')
			# no need to do pagination with search results as of yet.
			# paginator = Paginator(objects, 10)
			# page = request.GET.get('page')
			# try:
			# 	rtn_query = paginator.page(page)
			# except PageNotAnInteger:
			# # If page is not an integer, deliver first page.
			# 	rtn_query = paginator.page(1)
			# except EmptyPage:
			# # If page is out of range (e.g. 9999), deliver last page of results.
			# 	rtn_query = paginator.page(paginator.num_pages)

			return render(request, 'staffcom/list.html', {'inv_com': objects, 'viewname': 'Search'})