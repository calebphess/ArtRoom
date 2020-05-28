import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {UsersApiService} from './users/users-api.service'
import {ProductsApiService} from './products/products-api.service'

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [UsersApiService, ProductsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
