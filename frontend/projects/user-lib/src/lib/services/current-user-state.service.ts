import { Injectable } from '@angular/core';
import { State, Action, StateContext } from '@ngxs/store';
import { tap, catchError } from 'rxjs/operators';

import { CurrentUserState } from '../models/CurrentUserState';
import { SetCurrentUser, ClearCurrentUser, LoginUser, LogoutUser } from '../actions/current-user.actions';
import { UsersService } from '../services/users.service';

import { SetErrorMessage, ClearErrorMessage } from '@t4d-wnow/shared-lib';

@State<CurrentUserState>({
  name: 'currentUser',
  defaults: {
    username: '',
    userKind: '',
    displayName: '',
    roles: [] as string[],
  },
})
@Injectable({
  providedIn: 'root'
})
export class CurrentUserStateService {

  constructor(private usersSvc: UsersService) { }

  @Action(SetCurrentUser)
  setCurrentUser(ctx: StateContext<CurrentUserState>, action: SetCurrentUser) {
    ctx.patchState(action.currentUser);
  }

  @Action(ClearCurrentUser)
  clearCurrentUser(ctx: StateContext<CurrentUserState>) {
    ctx.patchState({
      username: '',
      userKind: '',
      displayName: '',
      roles: [] as string[],
    });
  }

  @Action(LoginUser)
  loginUser(ctx: StateContext<CurrentUserState>, action: LoginUser) {

    return this.usersSvc.loginEmployee(action.username, action.password).pipe(
      tap(() => {
        const currentUser = this.usersSvc.getCurrentUser();
        if (currentUser) {
          ctx.dispatch([
            new SetCurrentUser(currentUser),
            new ClearErrorMessage(),
          ]);
        } else {
          ctx.dispatch([
            new ClearCurrentUser(),
            new SetErrorMessage('Unable to retrieve current user.'),
          ]);
        }
      }),
      catchError((err: any) => {
        if (err.status === 404) {
          ctx.dispatch([
            new ClearCurrentUser(),
            new SetErrorMessage('Username and password not found.'),
          ]);
        } else {
          ctx.dispatch([
            new ClearCurrentUser(),
            new SetErrorMessage('Unknown login error.'),
          ]);
        }
        return err;
      }),
    );
  }

  @Action(LogoutUser)
  logoutUser(ctx: StateContext<CurrentUserState>) {
    ctx.dispatch([
      new ClearCurrentUser(),
      new ClearErrorMessage(),
    ]);
  }

}
