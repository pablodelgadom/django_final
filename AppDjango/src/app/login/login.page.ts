import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { RestServiceService } from '../services/rest-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  user= new FormControl('');
  password = new FormControl('');
  datos: any;
  imagen ="assets/icon/login.jpg";
  constructor(public restService: RestServiceService, private router: Router) { }

  ngOnInit() {
  }


  login(){
    console.log(this.user)
    this.restService.login(this.user.value, this.password.value)
    .then(data => {
      this.datos = data.Token;

      if(this.datos=!null){
        this.router.navigate(['list'])
  
      }
    });
    
  }
}
