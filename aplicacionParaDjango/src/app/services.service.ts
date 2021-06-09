import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  apiUrl = 'http://localhost:8100'

  datos_usuario : any;


  constructor(private http: HttpClient) { }

  async login(username, password) {
    return await new Promise<any>(resolve => {
      this.http.post(this.apiUrl + '/login',
        {
          username: username,
          password: password
        })
        .subscribe(data => {
          this.datos_usuario = data;
          console.log(this.datos_usuario);
          resolve(data);
        }, err => {
          console.log(err);
        });
    });
  }


  async getCitas() {
    return await new Promise<any>(resolve => {

      this.http.get(this.apiUrl + '/citas', {
        headers: new HttpHeaders().set('Authorization', 'Token ' + this.datos_usuario.Token),
      })
        .subscribe(data => {
          resolve(data);
        }, err => {
          console.log(err);
        });
    });
  }


}


