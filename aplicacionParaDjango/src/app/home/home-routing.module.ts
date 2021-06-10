import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePage } from './home.page';
import { LoginPage } from '../pages/login/login.page';

const routes: Routes = [
  {
    path: 'home',
    component: HomePage,
  },
  {
    path: '',
    component: LoginPage
    } ,
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomePageRoutingModule {}
