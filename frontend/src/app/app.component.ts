import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {UsersApiService} from './users/users-api.service';
import {User} from './users/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy{
  title = 'ArtRoom';
  usersListSubs: Subscription;
  usersList: User[];

  constructor(private usersApi: UsersApiService){}

  ngOnInit() {
    this.usersListSubs = this.usersApi.getUsers().subscribe(results => {
        this.usersList = results;
      },
      console.error  
    );
  }

  ngOnDestroy() {
    this.usersListSubs.unsubscribe();
  }
}
