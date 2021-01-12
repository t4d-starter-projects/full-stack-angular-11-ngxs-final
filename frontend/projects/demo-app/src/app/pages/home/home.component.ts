import { Component, OnInit } from '@angular/core';
import { Store, Select } from '@ngxs/store';

import { UsersService } from '@t4d-wnow/user-lib';
import { LoginForm } from '@t4d-wnow/user-lib';
import { Observable } from 'rxjs';
import { ClearErrorMessage } from '@t4d-wnow/shared-lib';
import { AppState } from '../../models/AppState';

import { CurrentUserState, LoginUser } from '@t4d-wnow/user-lib';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  @Select((state: { app: AppState }) => state.app.errorMessage)
  public errorMessage$: Observable<string> | undefined;

  @Select((state: { currentUser: CurrentUserState }) => state.currentUser)
  public currentUser$: Observable<CurrentUserState> | undefined;

  constructor(
    private usersSvc: UsersService,
    private store: Store,
  ) { }

  ngOnInit(): void {
  }

  doLogin(loginForm: LoginForm): void {

    this.store.dispatch(new LoginUser(loginForm.username, loginForm.password));

    // this.usersSvc.loginEmployee(loginForm.username, loginForm.password).subscribe({
    //   next: () => {
    //     // this.errorMessage = '';
    //     this.store.dispatch(new ClearErrorMessage());
    //   },
    //   error: (err) => {
    //     if (err.status === 404) {
    //       // this.errorMessage = 'Username and password not found.';
    //       this.store.dispatch(new SetErrorMessage('Username and password not found.'));
    //     } else {
    //       // this.errorMessage = 'Unknown login error.';
    //       this.store.dispatch(new SetErrorMessage('Unknown login error.'));
    //     }
    //   }
    // });
  }

  doClear(): void {
    console.log('clicked clear');
    // this.errorMessage = '';
    this.store.dispatch(new ClearErrorMessage());
  }

}
