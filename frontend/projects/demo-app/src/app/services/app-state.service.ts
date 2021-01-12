import { Injectable } from '@angular/core';
import { State, Action, StateContext } from '@ngxs/store';

import { AppState } from '../models/AppState';
import { SetErrorMessage, ClearErrorMessage } from '@t4d-wnow/shared-lib';

@State<AppState>({
  name: 'app',
  defaults: {
    errorMessage: '',
  }
})
@Injectable({
  providedIn: 'root'
})
export class AppStateService {

  constructor() { }

  @Action(SetErrorMessage)
  setErrorMessage(ctx: StateContext<AppState>, action: SetErrorMessage) {

    const state = ctx.getState();

    ctx.setState({
      ...state,
      errorMessage: action.errorMessage,
    });

  }

  @Action(ClearErrorMessage)
  clearErrorMessage(ctx: StateContext<AppState>) {
    ctx.patchState({
      errorMessage: ''
    });
  }
}
