import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  apiUrl = 'http://127.0.0.1:8000/api'

  datos_usuario : any;


  constructor(private http: HttpClient) { }

  async login(username, password) {
    return await new Promise<any>(resolve => {
      this.http.post(this.apiUrl + '/token',
        {
          user: 'Raul',
          password: 'usuario1'
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


