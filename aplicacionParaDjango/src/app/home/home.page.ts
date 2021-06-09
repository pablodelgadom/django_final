import { Component } from '@angular/core';
import { ServicesService } from '../services.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  citas : any[];

  constructor(public restService : ServicesService) {}


  ionViewWillEnter(){
    this.restService.getCitas()
    .then(data => {
      this.citas=data
      console.log(this.citas)
    });
  }

}
