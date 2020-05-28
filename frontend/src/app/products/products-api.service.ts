import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Product} from './product.model';

@Injectable()
export class ProductsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete product request.');
  }

  // GET list of products
  getProducts(): Observable<Product[]>{
    return this.http.get<Product[]>(`${API_URL}/products`).catch(ProductsApiService._handleError)
  }
}
