import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { tap, map } from 'rxjs/operators';

import { UserResult } from '../models/UserResult';
import { UserRefresh } from '../models/UserRefresh';
import { CurrentUser } from '../models/CurrentUser';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  private accessToken: string | null = null;
  private currentUser: CurrentUser | null = null;

  constructor(private httpClient: HttpClient) { }

  public loginEmployee(username: string, password: string): Observable<CurrentUser> {

    return this.httpClient
      .post<UserResult>(
        '/api/users/login',
        { username, password, kind: 'employee' })
      .pipe(
        tap(userResult => {
          this.accessToken = userResult.accessToken;
          localStorage.refreshToken = userResult.refreshToken;
        }),
        map(userResult => {
          const currentUser = new CurrentUser(userResult.username, userResult.userKind, userResult.displayName);
          userResult.roles.forEach(role => currentUser.addRole(role));
          return currentUser;
        }),
        tap(currentUser => {
          this.currentUser = currentUser
        }),
      );
  }

  public refreshUser(): Observable<Observable<boolean>> {
    return this.httpClient.get<UserRefresh>('/api/users/refresh').pipe(
      tap(userRefresh => {
        this.accessToken = userRefresh.accessToken;
        localStorage.refreshToken = userRefresh.refreshToken;
      }),
      map(() => of(true)),
    );
  }

  public changePassword(username: string, userKind: string, oldPassword: string, newPassword: string): Observable<{}> {
    return this.httpClient.post<{}>(
      '/api/users/change-password',
      {
        username, userKind, oldPassword, newPassword,
      });
  }

  public getCurrentUser(): CurrentUser | null {
    return this.currentUser;
  }

  public getAccessToken(): string | null {
    return this.accessToken;
  }

  public getRefreshToken(): string | null {
    return localStorage.refreshToken;
  }

  public logoutUser(): void {
    this.accessToken = null;
    this.currentUser = null;
    localStorage.refreshToken = null;
  }
}
