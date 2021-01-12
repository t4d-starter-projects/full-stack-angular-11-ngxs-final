import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';

import { UsersService } from './users.service';

@Injectable({
  providedIn: 'root'
})
export class AuthorizationInterceptorService implements HttpInterceptor {

  constructor(private usersSvc: UsersService) { }

  withAccessToken(req: HttpRequest<any>): HttpRequest<any> {
    return req.clone({
      headers: req.headers.set(
        'Authorization',
        'Bearer ' + this.usersSvc.getAccessToken(),
      ),
    });
  }

  withRefreshToken(req: HttpRequest<any>): HttpRequest<any> {
    return req.clone({
      method: 'GET',
      headers: req.headers.set(
        'Authorization',
        'Bearer ' + this.usersSvc.getRefreshToken(),
      ),
    });
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    if (req.url.endsWith('/api/users/login')) {
      return next.handle(req);
    }

    if (req.url.endsWith('/api/users/refresh')) {
      return next.handle(this.withRefreshToken(req));
    }

    return next.handle(this.withAccessToken(req)).pipe(
      catchError((err, caught) => {
        if (err instanceof HttpErrorResponse) {
          if (err.status === 401) {
            return this.usersSvc.refreshUser()
              .pipe(
                switchMap(() => next.handle(this.withAccessToken(req)))
              );
          } else {
            return throwError(err);
          }
        }
        return caught;
      })
    );

  }
}
