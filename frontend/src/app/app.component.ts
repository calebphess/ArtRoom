import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';
import { ProductsApiService } from './products/products-api.service';
import {Product} from './products/product.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy{
  title = 'ArtRoom';
  
  usersListSubs: Subscription;
  usersList: User[];

  productsListSubs: Subscription;
  productsList: Product[];

  constructor(private usersApi: UsersApiService, private productsApi: ProductsApiService){}

  ngOnInit() {
    this.usersListSubs = this.usersApi.getUsers().subscribe(results => {
        this.usersList = results;
      },
      console.error  
    );

    this.productsListSubs = this.productsApi.getProducts().subscribe(results => {
      this.productsList = results;
    },
    console.error  
  );
  }

  ngOnDestroy() {
    this.usersListSubs.unsubscribe();
    this.productsListSubs.unsubscribe();
  }
}
