import { Component, OnInit } from '@angular/core';
import { RestServiceService } from '../services/rest-service.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.page.html',
  styleUrls: ['./list.page.scss'],
})
export class ListPage implements OnInit {

  citas:any[];
  constructor(public restService: RestServiceService) { }

  ngOnInit() {
  }

  ionViewWillEnter(){
    this.restService.getCitas()
    .then(data => {
      this.citas=data
      console.log(this.citas)
    });
  }
}
