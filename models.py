# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource
import smtplib
import os
from pymsgbox import *


class schools9(models.Model):
    _name = 'schools9.schools9'

    


    @api.model
    def _default_image(self):
    	image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
    	return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    Name = fields.Char(string="Name",required=True)
    date_of_birth=fields.Date(string="DateOfBirth",required=True)
    student_gender= fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],required=True)
    address1=fields.Char(string="Perminent Address")
    address2=fields.Char(string="Prasent Address",required=True)
    phone_number=fields.Char(string="Mobile Number",)
    year_of_class=fields.Char(string="YearOfClass",required=True)
    Percentage=fields.Char(string="Percentage",required=True)
    email_id=fields.Char(string="Email-ID",required=True)
    Activities=fields.Char(string="Other Activities",)




    image = fields.Binary("Photo", default=_default_image, attachment=True,
        help="This field holds the image used as photo for the employee, limited to 1024x1024px.",required=True)


  
   



    def send_mail_template(self): 
        # Find the e-mail template
        template = self.env.ref('schools9.example_email_template1')
        # Send out the e-mail template to the user

        self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)
    





		
