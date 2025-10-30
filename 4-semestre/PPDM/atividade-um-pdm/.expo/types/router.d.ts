/* eslint-disable */
import * as Router from 'expo-router';

export * from 'expo-router';

declare module 'expo-router' {
  export namespace ExpoRouter {
    export interface __routes<T extends string | object = string> {
      hrefInputParams: { pathname: Router.RelativePathString, params?: Router.UnknownInputParams } | { pathname: Router.ExternalPathString, params?: Router.UnknownInputParams } | { pathname: `/`; params?: Router.UnknownInputParams; } | { pathname: `/../types/navigation`; params?: Router.UnknownInputParams; } | { pathname: `/github`; params?: Router.UnknownInputParams; } | { pathname: `/../components/PortfolioCard`; params?: Router.UnknownInputParams; } | { pathname: `/../components/FavoriteButton`; params?: Router.UnknownInputParams; } | { pathname: `/amandas-world`; params?: Router.UnknownInputParams; } | { pathname: `/_sitemap`; params?: Router.UnknownInputParams; };
      hrefOutputParams: { pathname: Router.RelativePathString, params?: Router.UnknownOutputParams } | { pathname: Router.ExternalPathString, params?: Router.UnknownOutputParams } | { pathname: `/`; params?: Router.UnknownOutputParams; } | { pathname: `/../types/navigation`; params?: Router.UnknownOutputParams; } | { pathname: `/github`; params?: Router.UnknownOutputParams; } | { pathname: `/../components/PortfolioCard`; params?: Router.UnknownOutputParams; } | { pathname: `/../components/FavoriteButton`; params?: Router.UnknownOutputParams; } | { pathname: `/amandas-world`; params?: Router.UnknownOutputParams; } | { pathname: `/_sitemap`; params?: Router.UnknownOutputParams; };
      href: Router.RelativePathString | Router.ExternalPathString | `/${`?${string}` | `#${string}` | ''}` | `/../types/navigation${`?${string}` | `#${string}` | ''}` | `/github${`?${string}` | `#${string}` | ''}` | `/../components/PortfolioCard${`?${string}` | `#${string}` | ''}` | `/../components/FavoriteButton${`?${string}` | `#${string}` | ''}` | `/amandas-world${`?${string}` | `#${string}` | ''}` | `/_sitemap${`?${string}` | `#${string}` | ''}` | { pathname: Router.RelativePathString, params?: Router.UnknownInputParams } | { pathname: Router.ExternalPathString, params?: Router.UnknownInputParams } | { pathname: `/`; params?: Router.UnknownInputParams; } | { pathname: `/../types/navigation`; params?: Router.UnknownInputParams; } | { pathname: `/github`; params?: Router.UnknownInputParams; } | { pathname: `/../components/PortfolioCard`; params?: Router.UnknownInputParams; } | { pathname: `/../components/FavoriteButton`; params?: Router.UnknownInputParams; } | { pathname: `/amandas-world`; params?: Router.UnknownInputParams; } | { pathname: `/_sitemap`; params?: Router.UnknownInputParams; };
    }
  }
}
