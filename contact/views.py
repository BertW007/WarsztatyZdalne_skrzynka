from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q

from contact.models import Person, Address, Telephone, Email, Group


@method_decorator(csrf_exempt, name='dispatch')
class Main(View):

    def get(self, request):
        people = Person.objects.order_by('last_name', 'first_name')
        groups = Group.objects.order_by('name')
        return render(request, 'html_main.html', {'people': people,
                                                  'groups': groups})

    def post(self, request):
        if "show_group" in request.POST:
            group_id = request.POST.get("group_id")
            return self.get_groups(request, group_id)
        elif "show_person" in request.POST:
            search_string = request.POST.get("search_person")
            return self.search(request, search_string)

    def get_groups(self, request, group_id):
        group = Group.objects.get(pk=int(group_id))
        people = group.people.all().order_by('last_name', 'first_name')
        groups = Group.objects.order_by('name')
        return render(request, 'html_main.html', {'people': people,
                                                  'groups': groups})

    def search(self, request, search_string):
        groups = Group.objects.order_by('name')
        query = search_string.split()
        people = []
        for term in query:
            people = Person.objects.filter(
                Q(first_name__icontains=term) |
                Q(last_name__icontains=term))\
                .order_by('last_name', 'first_name')
        # Jeśli chcemy wyszukiwać OR, należy zmienić nazwy zmiennych
        # i dodać poniższe linijki. Problem pozostaje z posortowaniem
        # uzyskanych wyników.
            # for person in people_found:
            #     people.add(person)
        return render(request, 'html_main.html', {'people': people,
                                                  'groups': groups})


def show_person(request, person_id):
    person_id = int(person_id)
    person = Person.objects.get(pk=person_id)
    addresses = person.address_set.all()
    telephones = person.telephone_set.all()
    emails = person.email_set.all()
    groups = person.group_set.all().order_by('name')
    return render(request, 'html_person_show', {'person': person,
                                                'addresses': addresses,
                                                'telephones': telephones,
                                                'emails': emails,
                                                'groups': groups})


def modify_person(request, person_id):
    person_id = int(person_id)
    person = Person.objects.get(pk=person_id)
    addresses = person.address_set.all()
    telephones = person.telephone_set.all()
    emails = person.email_set.all()
    groups = person.group_set.all().order_by('name')
    return render(request, 'html_person_modify', {'person': person,
                                                  'addresses': addresses,
                                                  'telephones': telephones,
                                                  'emails': emails,
                                                  'groups': groups})


@method_decorator(csrf_exempt, name='dispatch')
class AddEditPerson(View):

    def get(self, request, person_id=None):
        if person_id:
            person_id = int(person_id)
            person = Person.objects.get(pk=person_id)
            return render(request, 'html_person_add_edit', {'person': person})
        else:
            return render(request, 'html_person_add_edit')

    def post(self, request, person_id=None):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        if person_id:
            person_id = int(person_id)
            person = Person.objects.get(pk=person_id)
            person.first_name = first_name
            person.last_name = last_name
            person.save()
            return HttpResponseRedirect('/show/' + str(person_id))
        else:
            Person.objects.create(first_name=first_name, last_name=last_name)
            return HttpResponseRedirect('/')


def delete_person(request, person_id):
    person_id = int(person_id)
    person = Person.objects.get(pk=person_id)
    person.delete()
    return HttpResponseRedirect('/')


@method_decorator(csrf_exempt, name='dispatch')
class AddEditAddress(View):

    def get(self, request, person_id, address_id=None):
        if address_id:
            address_id = int(address_id)
            address = Address.objects.get(pk=address_id)
            return render(request, 'html_address_add_edit', {'address': address})
        else:
            return render(request, 'html_address_add_edit')

    def post(self, request, person_id, address_id=None):
        person = Person.objects.get(pk=int(person_id))
        city = request.POST.get("city")
        street = request.POST.get("street")
        street_number = request.POST.get("street_number")
        home_number = request.POST.get("home_number")
        if address_id:
            address_id = int(address_id)
            address = Address.objects.get(pk=address_id)
            address.city = city
            address.street = street
            address.street_number = street_number
            address.home_number = home_number
            address.save()
            return HttpResponseRedirect('/show/' + person_id)
        else:
            Address.objects.create(person_id=person,
                                   city=city,
                                   street=street,
                                   street_number=street_number,
                                   home_number=home_number)
            return HttpResponseRedirect('/modify/' + person_id)


def delete_address(request, person_id, address_id):
    address_id = int(address_id)
    address = Address.objects.get(pk=address_id)
    address.delete()
    return HttpResponseRedirect('/modify/' + person_id)


@method_decorator(csrf_exempt, name='dispatch')
class AddEditTelephone(View):

    def get(self, request, person_id, telephone_id=None):
        if telephone_id:
            telephone_id = int(telephone_id)
            telephone = Telephone.objects.get(pk=telephone_id)
            return render(request, 'html_telephone_add_edit', {'telephone': telephone})
        else:
            return render(request, 'html_telephone_add_edit')

    def post(self, request, person_id, telephone_id=None):
        person = Person.objects.get(pk=int(person_id))
        number = request.POST.get("number")
        type = request.POST.get("type")
        if telephone_id:
            telephone_id = int(telephone_id)
            telephone = Telephone.objects.get(pk=telephone_id)
            telephone.number = number
            telephone.type = type
            telephone.save()
            return HttpResponseRedirect('/show/' + person_id)
        else:
            Telephone.objects.create(person_id=person,
                                   number=number,
                                   type=type)
            return HttpResponseRedirect('/modify/' + person_id)


def delete_telephone(request, person_id, telephone_id):
    telephone_id = int(telephone_id)
    telephone = Telephone.objects.get(pk=telephone_id)
    telephone.delete()
    return HttpResponseRedirect('/modify/' + person_id)


@method_decorator(csrf_exempt, name='dispatch')
class AddEditEmail(View):

    def get(self, request, person_id, email_id=None):
        if email_id:
            email_id = int(email_id)
            email = Email.objects.get(pk=email_id)
            return render(request, 'html_email_add_edit', {'email': email})
        else:
            return render(request, 'html_email_add_edit')

    def post(self, request, person_id, email_id=None):
        person = Person.objects.get(pk=int(person_id))
        address = request.POST.get("address")
        type = request.POST.get("type")
        if email_id:
            email_id = int(email_id)
            email = Email.objects.get(pk=email_id)
            email.address = address
            email.type = type
            email.save()
            return HttpResponseRedirect('/show/' + person_id)
        else:
            Email.objects.create(person_id=person,
                                 address=address,
                                 type=type)
            return HttpResponseRedirect('/modify/' + person_id)


def delete_email(request, person_id, email_id):
    email_id = int(email_id)
    email = Email.objects.get(pk=email_id)
    email.delete()
    return HttpResponseRedirect('/modify/' + person_id)


@method_decorator(csrf_exempt, name='dispatch')
class AddToGroup(View):

    def get(self, request, person_id):
        groups = Group.objects.order_by('name')
        return render(request, 'html_addtogroup', {'person_id': person_id,
                                                   'groups': groups})

    def post(self, request, person_id):
        person = Person.objects.get(pk=int(person_id))
        group_id = request.POST.get("group_id")
        try:
            group_id = int(group_id)
        except (ValueError, TypeError):
            return HttpResponseRedirect('/person/{}/group/add'.format(person_id))
        group = Group.objects.get(pk=group_id)
        group.people.add(person)
        return HttpResponseRedirect('/modify/' + person_id)


@method_decorator(csrf_exempt, name='dispatch')
class CreateGroup(View):

    def get(self, request, person_id):
        return render(request, 'html_creategroup')

    def post(self, request, person_id):
        name = request.POST.get("name")
        description = request.POST.get("description")
        Group.objects.create(name=name,
                             description=description)
        return HttpResponseRedirect('/person/{}/group/add'.format(person_id))


def remove_from_group(request, person_id, group_id):
    group_id = int(group_id)
    person_id = int(person_id)
    group = Group.objects.get(pk=group_id)
    person = Person.objects.get(pk=person_id)
    group.people.remove(person)
    return HttpResponseRedirect('/modify/' + str(person_id))


